// React Theme — extracted from https://graft.framer.website/
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '26': string;
    '40': string;
    '100': string;
    '180': string;
    '585.57': string;
 *   };
 *   space: {
    '1': string;
    '5': string;
    '25': string;
    '30': string;
    '35': string;
    '50': string;
    '60': string;
    '70': string;
    '100': string;
    '124': string;
    '131': string;
    '142': string;
    '200': string;
    '218': string;
    '360': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    xl: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
    lg: string;
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
    "primary": "#392615",
    "secondary": "#0000ee",
    "accent": "#736557",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#585048",
    "neutral300": "#c2bbb5",
    "neutral400": "#767676",
    "neutral500": "#f6f6f6",
    "neutral600": "#d9d9d9"
  },
  "fonts": {
    "body": "'Inter Tight', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "26": "26px",
    "40": "40px",
    "100": "100px",
    "180": "180px",
    "585.57": "585.57px"
  },
  "space": {
    "1": "1px",
    "5": "5px",
    "25": "25px",
    "30": "30px",
    "35": "35px",
    "50": "50px",
    "60": "60px",
    "70": "70px",
    "100": "100px",
    "124": "124px",
    "131": "131px",
    "142": "142px",
    "200": "200px",
    "218": "218px",
    "360": "360px"
  },
  "radii": {
    "sm": "3px",
    "md": "10px",
    "lg": "15px",
    "xl": "22px",
    "full": "200px"
  },
  "shadows": {
    "sm": "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "xs": "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px",
    "lg": "rgba(0, 0, 0, 0.25) 0px 10px 20px 0px"
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
      "main": "#392615",
      "light": "hsl(28, 46%, 30%)",
      "dark": "hsl(28, 46%, 10%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "400",
      "lineHeight": "44px"
    },
    "h2": {
      "fontSize": "26px",
      "fontWeight": "400",
      "lineHeight": "28.6px"
    },
    "body1": {
      "fontSize": "18px",
      "fontWeight": "500",
      "lineHeight": "23.4px"
    }
  },
  "shape": {
    "borderRadius": 7
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px",
    "rgba(0, 0, 0, 0.25) 0px 10px 20px 0px"
  ]
};

export default theme;
