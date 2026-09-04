// React Theme — extracted from https://www.palais.bio/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '15': string;
    '16': string;
    '17': string;
    '24': string;
    '28': string;
    '32': string;
    '33': string;
    '46': string;
    '48': string;
    '50': string;
    '72': string;
    '73': string;
 *   };
 *   space: {
    '2': string;
    '30': string;
    '37': string;
    '48': string;
    '64': string;
    '70': string;
    '80': string;
    '90': string;
    '100': string;
    '104': string;
    '110': string;
    '120': string;
    '128': string;
    '144': string;
    '150': string;
    '160': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    md: string;
    xl: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#234386",
    "secondary": "#61a229",
    "accent": "#00578a",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#212529",
    "neutral300": "#333333",
    "neutral400": "#f3f5f7",
    "neutral500": "#3a4856",
    "neutral600": "#e3e1e8",
    "neutral700": "#898989",
    "neutral800": "#111111"
  },
  "fonts": {
    "body": "'Sandman_Fill', sans-serif"
  },
  "fontSizes": {
    "15": "15px",
    "16": "16px",
    "17": "17px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "33": "33px",
    "46": "46px",
    "48": "48px",
    "50": "50px",
    "72": "72px",
    "73": "73px"
  },
  "space": {
    "2": "2px",
    "30": "30px",
    "37": "37px",
    "48": "48px",
    "64": "64px",
    "70": "70px",
    "80": "80px",
    "90": "90px",
    "100": "100px",
    "104": "104px",
    "110": "110px",
    "120": "120px",
    "128": "128px",
    "144": "144px",
    "150": "150px",
    "160": "160px"
  },
  "radii": {
    "xs": "2px",
    "sm": "5px",
    "md": "8px",
    "lg": "16px",
    "full": "50px"
  },
  "shadows": {
    "sm": "rgb(22, 22, 22) 2px 2px 5px 2px",
    "md": "rgba(172, 171, 171, 0.3) 0px -1px 10px 0px",
    "xl": "rgba(0, 0, 0, 0.16) -14px 10px 49px 0px"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#234386",
      "light": "hsl(221, 59%, 48%)",
      "dark": "hsl(221, 59%, 18%)"
    },
    "secondary": {
      "main": "#61a229",
      "light": "hsl(92, 60%, 55%)",
      "dark": "hsl(92, 60%, 25%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#fbf9f6"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Lucida Grande', sans-serif",
    "h1": {
      "fontSize": "33px",
      "fontWeight": "400",
      "lineHeight": "39px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgb(22, 22, 22) 2px 2px 5px 2px",
    "rgba(172, 171, 171, 0.3) 0px -1px 10px 0px",
    "rgba(12, 25, 51, 0.08) 4px 8px 24px 0px",
    "rgba(0, 0, 0, 0.13) 10px 10px 26px 0px",
    "rgba(0, 0, 0, 0.05) 0px 20px 27px 0px"
  ]
};

export default theme;
