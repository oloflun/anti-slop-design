// React Theme — extracted from https://dixhectares.com/en
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
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '10': string;
    '11': string;
    '12': string;
    '14': string;
    '16': string;
    '20': string;
    '22': string;
    '28': string;
    '40': string;
    '46': string;
 *   };
 *   space: {
    '1': string;
    '56': string;
    '72': string;
    '80': string;
    '105': string;
    '111': string;
    '120': string;
    '144': string;
    '152': string;
    '177': string;
    '324': string;
    '360': string;
    '399': string;
 *   };
 *   radii: {
    xs: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    md: string;
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
    "primary": "#a85435",
    "secondary": "#555114",
    "accent": "#efe5d7",
    "background": "#efe5d7",
    "foreground": "#000000",
    "neutral50": "#e5e7eb",
    "neutral100": "#000000",
    "neutral200": "#ffffff",
    "neutral300": "#6b7280"
  },
  "fonts": {
    "body": "'GTStandard-M', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "11": "11px",
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "20": "20px",
    "22": "22px",
    "28": "28px",
    "40": "40px",
    "46": "46px"
  },
  "space": {
    "1": "1px",
    "56": "56px",
    "72": "72px",
    "80": "80px",
    "105": "105px",
    "111": "111px",
    "120": "120px",
    "144": "144px",
    "152": "152px",
    "177": "177px",
    "324": "324px",
    "360": "360px",
    "399": "399px"
  },
  "radii": {
    "xs": "2px",
    "full": "9999px"
  },
  "shadows": {
    "sm": "rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px",
    "md": "rgba(63, 63, 68, 0.4) 0px 4px 10px 0px"
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
      "main": "#a85435",
      "light": "hsl(16, 52%, 58%)",
      "dark": "hsl(16, 52%, 28%)"
    },
    "secondary": {
      "main": "#555114",
      "light": "hsl(56, 62%, 36%)",
      "dark": "hsl(56, 62%, 10%)"
    },
    "background": {
      "default": "#efe5d7",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#a85435"
    }
  },
  "typography": {
    "fontFamily": "'GTStandard-M', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "400",
      "lineHeight": "18px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "400",
      "lineHeight": "32px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "23px"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "400",
      "lineHeight": "18.4px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": [
    "rgb(255, 255, 255) 0px 0px 0px 0px, rgba(59, 130, 246, 0.5) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px",
    "rgba(63, 63, 68, 0.4) 0px 4px 10px 0px"
  ]
};

export default theme;
